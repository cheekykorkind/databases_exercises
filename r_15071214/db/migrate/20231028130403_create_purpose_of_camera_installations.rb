class CreatePurposeOfCameraInstallations < ActiveRecord::Migration[7.1]
  def change
    create_table :purpose_of_camera_installations do |t|
      t.string :purpose

      t.timestamps
    end
  end
end
