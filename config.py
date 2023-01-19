SECRET_KEY = 'teste'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'projetos',
        senha = 'admin',
        servidor = 'localhost',
        database = 'jogoteca'
    )