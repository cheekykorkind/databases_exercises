class Project < ApplicationRecord
  has_many :sensors, dependent: :destroy
end
