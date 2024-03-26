import os


directories = ['project_code', 'project_code/src']
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

src_files = [
    ('project_code/src/UserInputParser.py', ''),
    ('project_code/src/InstanceCreator.py', ''),
    ('project_code/src/UserFactory.py', '')
]
for file, content in src_files:
    with open(file, 'w') as f:
        f.write(content)

print("Project directory structure created successfully.")
