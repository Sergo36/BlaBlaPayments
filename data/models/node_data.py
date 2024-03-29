from peewee import AutoField, TextField, ForeignKeyField

from data.models.base_model import BaseModel
from data.models.node import Node


class NodeData(BaseModel):
    id = AutoField(column_name='id')
    node_id = ForeignKeyField(column_name='node_id', model=Node)
    name = TextField(column_name='name')
    data = TextField(column_name='data')

    class Meta:
        table_name = 'node_data'
