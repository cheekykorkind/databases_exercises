class Facility < ApplicationRecord
  belongs_to :management_agency
  belongs_to :purpose_of_camera_installation
  has_many :camera_location
end
