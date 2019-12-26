#!/usr/bin/env bash
python -m coverage run --source wpa_status -m py.test
coverage report
