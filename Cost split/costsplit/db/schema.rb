# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2018_11_28_205417) do

  create_table "athletes", force: :cascade do |t|
    t.string "name"
    t.string "email"
    t.integer "phone"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.text "schedule"
    t.string "all_teams"
  end

  create_table "data", force: :cascade do |t|
    t.string "stdName"
    t.float "calculation"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "factivities", force: :cascade do |t|
    t.string "stdName"
    t.string "activity"
    t.integer "exertion"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "fmornings", force: :cascade do |t|
    t.string "stdName"
    t.integer "urineCol"
    t.float "sleepTime"
    t.integer "bodySoreness"
    t.datetime "subDatetime"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "taggings", force: :cascade do |t|
    t.integer "post_id"
    t.integer "athlete_id"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["athlete_id"], name: "index_taggings_on_athlete_id"
    t.index ["post_id"], name: "index_taggings_on_post_id"
  end

  create_table "teams", force: :cascade do |t|
    t.string "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "textstrings", force: :cascade do |t|
    t.string "textstring"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "users", force: :cascade do |t|
    t.text "username"
    t.text "password"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

end
