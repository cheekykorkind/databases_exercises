class CameraLocation < ApplicationRecord
  belongs_to :facility
  belongs_to :which_direction
end
