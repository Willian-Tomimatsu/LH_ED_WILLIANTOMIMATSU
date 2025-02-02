#!/bin/bash

if [ ! -s /caminho/para/arquivo.csv ]; then
  echo "O arquivo está vazio. Criando um arquivo CSV vazio com cabeçalho."
  echo "coluna1,coluna2,coluna3" > /caminho/para/arquivo.csv  # Cabeçalhos de exemplo
fi
