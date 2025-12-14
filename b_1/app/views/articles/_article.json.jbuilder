json.extract! article, :id, :project_id, :content, :created_at, :updated_at
json.url article_url(article, format: :json)
