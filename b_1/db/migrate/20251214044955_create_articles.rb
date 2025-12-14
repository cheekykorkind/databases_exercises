class CreateArticles < ActiveRecord::Migration[8.1]
  def change
    create_table :articles do |t|
      t.references :project, null: false, foreign_key: true
      t.text :content

      t.timestamps
    end
  end
end
