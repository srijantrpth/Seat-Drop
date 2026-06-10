from celery import shared_task
import time

@shared_task
def send_completion_email(order_id):
    time.sleep(10)  # Simulate delay
    print(f"Completion email sent for order: {order_id}")