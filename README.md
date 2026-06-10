# Seatdrop 🎟️

A high-concurrency, distributed ticketing backend API built to handle massive traffic spikes and prevent double-booking during high-demand event drops.

## 🚀 System Architecture

Seatdrop bypasses standard CRUD operations by implementing a decoupled, async-first architecture:
* **Web Framework:** Django / Django REST Framework (DRF)
* **Primary Database:** PostgreSQL
* **Message Broker:** Redis
* **Background Workers:** Celery

## ⚙️ Core Technical Achievements

* **Concurrency Control & Race Condition Prevention:** Implemented PostgreSQL row-level locks (`select_for_update`) combined with Django atomic transactions to guarantee thread safety. This mathematically prevents overselling capacity when thousands of users attempt to purchase the exact same ticket at the exact same millisecond.
* **Asynchronous Background Processing:** Completely decoupled heavy I/O operations (like PDF ticket generation and SMTP email dispatch) from the main HTTP request thread. Utilized Celery and Redis to handle these tasks in the background, triggered safely via `transaction.on_commit()` to ensure data integrity.
* **Optimized Database Transactions:** Replaced standard iterative database saves with highly optimized in-memory Python list comprehensions and `bulk_create` operations, drastically reducing database hits and maximizing speed during multi-ticket checkouts.
* **Event-Driven Capacity Management:** Engineered custom Django signals equipped with aggregate queries to dynamically compute venue capacity and toggle "Sold Out" statuses in real-time.
