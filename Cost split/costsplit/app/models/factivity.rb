class Factivity < ApplicationRecord
  validates :stdName, presence:true
  validates :activity, presence:true
  validates :exertion, presence:true
end
