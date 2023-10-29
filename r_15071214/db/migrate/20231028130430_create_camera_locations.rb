class CreateCameraLocations < ActiveRecord::Migration[7.1]
  def change
    create_table :camera_locations do |t|
      t.string :location
      t.belongs_to :facility, null: false, foreign_key: true
      t.belongs_to :which_direction, null: false, foreign_key: true
      t.integer :installation_year
      t.float :latitude
      t.float :longitude

      t.timestamps
    end
  end
end
