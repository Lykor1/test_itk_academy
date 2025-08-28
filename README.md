# Тестовое задание для ITK Академии

## Описание:
Здесь реализована система работы с балансом (отображение) и операции добавления/уменьшения баланса.
Стэк: Django REST Framework + PostgreSQL.
Всё запускается в Docker Compose.
Также реализованы тесты для эндпоинтов.

## Возможности:
1. Отображение баланса: api/v1/wallet/<wallet_uuid>/
2. Операции DEPOSIT/ WITHDRAW: api/v1/wallet/<wallet_uuid>/operation/
