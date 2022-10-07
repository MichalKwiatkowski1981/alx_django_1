import faker
f = faker.Faker('pl-PL')
print(f.name())
print(f.name())
print(f.name())
print(f.name())
print(f.paragraph(6))
content = '\n\n'.join([f.paragraph(6) for _ in range(8)])
print(content)


