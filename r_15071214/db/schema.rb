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

ActiveRecord::Schema[7.1].define(version: 2023_10_28_130430) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "camera_locations", force: :cascade do |t|
    t.string "location"
    t.bigint "facility_id", null: false
    t.bigint "which_direction_id", null: false
    t.integer "installation_year"
    t.float "latitude"
    t.float "longitude"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["facility_id"], name: "index_camera_locations_on_facility_id"
    t.index ["which_direction_id"], name: "index_camera_locations_on_which_direction_id"
  end

  create_table "facilities", force: :cascade do |t|
    t.string "name"
    t.bigint "management_agency_id", null: false
    t.bigint "purpose_of_camera_installation_id", null: false
    t.integer "number_of_cameras"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["management_agency_id"], name: "index_facilities_on_management_agency_id"
    t.index ["purpose_of_camera_installation_id"], name: "index_facilities_on_purpose_of_camera_installation_id"
  end

  create_table "management_agencies", force: :cascade do |t|
    t.string "name"
    t.bigint "national_police_agency_id", null: false
    t.bigint "police_station_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["national_police_agency_id"], name: "index_management_agencies_on_national_police_agency_id", unique: true
    t.index ["police_station_id"], name: "index_management_agencies_on_police_station_id", unique: true
  end

  create_table "national_police_agencies", force: :cascade do |t|
    t.string "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "police_stations", force: :cascade do |t|
    t.string "name"
    t.bigint "national_police_agency_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["national_police_agency_id"], name: "index_police_stations_on_national_police_agency_id"
  end

  create_table "purpose_of_camera_installations", force: :cascade do |t|
    t.string "purpose"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "which_directions", force: :cascade do |t|
    t.string "direction"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_foreign_key "camera_locations", "facilities"
  add_foreign_key "camera_locations", "which_directions"
  add_foreign_key "facilities", "management_agencies"
  add_foreign_key "facilities", "purpose_of_camera_installations"
  add_foreign_key "management_agencies", "national_police_agencies"
  add_foreign_key "management_agencies", "police_stations"
  add_foreign_key "police_stations", "national_police_agencies"
end
