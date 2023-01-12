#!/usr/bin/env python

"""email span
"""
__version__ = "0.1.0"
__author__ = "Alberto"

email_tmpl = """
                Olá, %(nome)s!

                Tem interesse em comprar %(produto)s?

                Este produto é ótimo para resolver %(texto)s

                Clique agora em %(link)s

                Apenas %(quantidade)d disponiveis!

                Preço promocional: %(preco).2f
            """

clientes = ["Alberto", "Beto", "Julia"]

for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "problemas de escrita.",
            "link": "https://canetalegal.com",
            "quantidade": 1,
            "preco": 50.5
        }
    )
