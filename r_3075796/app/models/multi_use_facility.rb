class MultiUseFacility < ApplicationRecord
  belongs_to :main_purpose
  belongs_to :address
end
