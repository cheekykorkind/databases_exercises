class Sensor < ApplicationRecord
  belongs_to :project
  has_many :sensor_datums, dependent: :destroy
end
