from faker import Faker
from .models import Response

fake = Faker()

def seed_responses(n=10):
    for _ in range(n):
        Response.objects.create(
            prompt=fake.text(max_nb_chars=100),
            response_text=fake.text(max_nb_chars=200),
            model_used=f"Model-{fake.random_int(1, 5)}",
            status=fake.random_element(elements=('completed', 'in_progress')),
            processing_time=round(fake.random_number(digits=2, fix_len=True) / 100, 2),
        )
    print(f"Seeded {n} responses.")
