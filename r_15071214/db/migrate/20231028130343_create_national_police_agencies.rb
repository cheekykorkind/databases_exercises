class CreateNationalPoliceAgencies < ActiveRecord::Migration[7.1]
  def change
    create_table :national_police_agencies do |t|
      t.string :name

      t.timestamps
    end
  end
end
