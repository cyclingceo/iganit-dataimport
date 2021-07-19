from yoyo import read_migrations, get_backend

backend = get_backend('postgres://postgres:docker@localhost:5532/iganit-master-data')
migrations = read_migrations('./migrations')
with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))
# backend.rollback_migrations(backend.to_rollback(migrations))