class CreateSensors < ActiveRecord::Migration[8.1]
  def change
    create_table :sensors do |t|
      t.references :project, null: false, foreign_key: true
      t.string :name

      t.timestamps
    end
  end
end
