class CreateFacilities < ActiveRecord::Migration[7.1]
  def change
    create_table :facilities do |t|
      t.string :name
      t.belongs_to :management_agency, null: false, foreign_key: true
      t.belongs_to :purpose_of_camera_installation, null: false, foreign_key: true
      t.integer :number_of_cameras

      t.timestamps
    end
  end
end
