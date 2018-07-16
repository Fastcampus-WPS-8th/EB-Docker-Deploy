#!/usr/bin/env bash
# requirements.txt만들기
pipenv lock --requirements > requirements.txt

# .secrets와 requirements를 staging area에 추가
git add -f .secrets/ requirements.txt

# eb deploy실행
eb deploy --profile fc-8th-eb --staged

# .secrets와 requirements를 staging area에서 제거
git reset HEAD .secrets/ requirements.txt

# requirements.txt삭제
rm requirements.txt
