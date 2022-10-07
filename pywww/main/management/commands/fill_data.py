from django.core.management.base import BaseCommand
from posts.models import Post
import faker

f = faker.Faker('pl-Pl')


class Command(BaseCommand):
    help = "Dodaję 3 nowe posty."

    def handle(self, *args, **options):
        for _ in range(3):
            p = Post()
            p.title = f.paragraph(2)
            p.content = '\n\n'.join([f.paragraph(6) for _ in range(5)])
            p.published = f.boolean(70)
            p.save()
