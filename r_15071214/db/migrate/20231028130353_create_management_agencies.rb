class CreateManagementAgencies < ActiveRecord::Migration[7.1]
  def change
    create_table :management_agencies do |t|
      t.string :name
      t.belongs_to :national_police_agency, index: {:unique=>true}, null: false, foreign_key: true
      t.belongs_to :police_station, index: {:unique=>true}, null: false, foreign_key: true

      t.timestamps
    end
  end
end
