class CreateSensorData < ActiveRecord::Migration[8.1]
  def change
    create_table :sensor_data do |t|
      t.references :sensor, null: false, foreign_key: true
      t.json :data

      t.timestamps
    end
  end
end
