class Team < ApplicationRecord
  has_many :taggings
  has_many :athletes, through: :taggings
end
