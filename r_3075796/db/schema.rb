# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.1].define(version: 20_231_030_130_514) do
  # These are extensions that must be enabled in order to support this database
  enable_extension 'plpgsql'

  create_table 'addresses', force: :cascade do |t|
    t.string 'address'
    t.datetime 'created_at', null: false
    t.datetime 'updated_at', null: false
  end

  create_table 'main_purposes', force: :cascade do |t|
    t.string 'purpose'
    t.datetime 'created_at', null: false
    t.datetime 'updated_at', null: false
  end

  create_table 'multi_use_facilities', force: :cascade do |t|
    t.string 'name'
    t.string 'total_floor_area'
    t.string 'description'
    t.bigint 'main_purpose_id', null: false
    t.bigint 'address_id', null: false
    t.datetime 'created_at', null: false
    t.datetime 'updated_at', null: false
    t.index ['address_id'], name: 'index_multi_use_facilities_on_address_id'
    t.index ['main_purpose_id'], name: 'index_multi_use_facilities_on_main_purpose_id'
  end

  add_foreign_key 'multi_use_facilities', 'addresses'
  add_foreign_key 'multi_use_facilities', 'main_purposes'
end
