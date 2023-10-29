class CreatePoliceStations < ActiveRecord::Migration[7.1]
  def change
    create_table :police_stations do |t|
      t.string :name
      t.belongs_to :national_police_agency, null: false, foreign_key: true

      t.timestamps
    end
  end
end
