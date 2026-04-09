#!/bin/bash
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo "Ошибка. Скрипт запущен не root." >&2
    fi
}
check_root
