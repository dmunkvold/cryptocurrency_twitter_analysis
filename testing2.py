from dataset_builder.dataset_builder import *

d_builder = DataSetBuilder('ETH', ['eth', 'ethereum'])
dataset = d_builder.generate_data_set('11/18/2018', 10, 0)
print(dataset)
