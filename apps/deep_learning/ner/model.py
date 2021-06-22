"""model.py
~~~~~~~~~~~~~~~~~~~~~~
基于预训练模型的命名实体识别（ner）模型。

:copyright: (c) 2019 by Zhichao Xia
:modified: 2021-06-17

:TODO:
"""
import torch.nn as nn
from transformers import AlbertModel, AlbertPreTrainedModel


class AlbertTokenClassifier(AlbertPreTrainedModel):
    """基于Albert的NER识别基本版"""

    def __init__(self, config):
        super(AlbertTokenClassifier, self).__init__(config)  # 继承父类AlbertPreTrainedModel
        self.num_labels = config.num_labels
        self.albert = AlbertModel(config)
        self.dropout = nn.Dropout(.1)
        self.classifier = nn.Linear(config.hidden_size, config.num_labels)
        self.init_weights()  # 权重初始化

    def forward(self, input_ids, attention_mask=None, mems=None, perm_mask=None, target_mapping=None,
                token_type_ids=None, input_mask=None, ead_mask=None, labels=None):
        """待补充"""
        outputs = self.albert(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        output = outputs[0]  # outputs[0]为last_hidden_state,即最后一层隐藏层状态
        seq_outputs = self.dropout(output)  # 对output进行dropout处理，防止过拟合
        logits = self.classifier(seq_outputs)  # logits可以理解为输出层的内容
        outputs = (logits,) + outputs[1:]  # 元组拼接
        if labels is not None:
            loss_fct = nn.CrossEntropyLoss()  # 使用交叉熵损失
            if attention_mask is not None:
                pass

