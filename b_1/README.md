# 커멘드 기록
bundle exec rails db:create db:migrate
bundle exec rails s -b 0.0.0.0


# 1. Project 생성 (name, memo)
bundle exec rails g scaffold Project name:string memo:text

# 2. Article 생성 (Project에 소속됨)
bundle exec rails g scaffold Article project:references content:text

# 3. Comment 생성 (Article에 소속됨)
bundle exec rails g scaffold Comment article:references content:text

# 4. 데이터베이스 마이그레이션 적용
bundle exec rails db:migrate