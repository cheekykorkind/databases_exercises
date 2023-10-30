class CreateMultiUseFacilities < ActiveRecord::Migration[7.1]
  def change
    create_table :multi_use_facilities do |t|
      t.string :name
      t.string :total_floor_area
      t.string :description
      t.belongs_to :main_purpose, null: false, foreign_key: true
      t.belongs_to :address, null: false, foreign_key: true

      t.timestamps
    end
  end
end
