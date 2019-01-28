class Tagging < ApplicationRecord
  belongs_to :team
  belongs_to :athlete
end
