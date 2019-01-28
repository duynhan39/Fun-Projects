class Fmorning < ApplicationRecord
  validates :stdName, presence: true
  validates :urineCol, presence: true
  validates :sleepTime, presence: true
  validates :bodySoreness, presence: true
end
