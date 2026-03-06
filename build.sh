#!/usr/bin/env bash
# Hata olursa dur
set -o errexit

# Bağımlılıkları yükle
pip install -r requirements.txt

# Statik dosyaları topla
python manage.py collectstatic --no-input

# Veritabanını güncelle (Shell yerine burada yapıyoruz)
python manage.py migrate