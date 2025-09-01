yaml_content = """
train: /content/dataset/images/train
val: /content/dataset/images/val

nc: 3
names: ['Laptop', 'Phone', 'Tab']
"""

with open("/content/dataset/data.yaml", "w") as f:
    f.write(yaml_content)
