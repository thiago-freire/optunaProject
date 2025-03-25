from optuna.storages import RDBStorage
from optuna_dashboard import run_server

storage = RDBStorage("postgresql://postgres:postgres@192.168.200.169/optuna_thiago")
run_server(storage)