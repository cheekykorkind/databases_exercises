require 'rails_helper'

RSpec.describe CameraLocation do
  describe '#create' do
    context '부모 관계인 Facility와 WhichDirection를 미리 만들지 않아서' do
      let(:create_param) { { location: 'location1', facility_id: 1, which_direction_id: 1 } }
      let(:expected) { 'Validation failed: Facility must exist, Which direction must exist' }
      it 'create 불가능' do
        expect { CameraLocation.create!(create_param) }.to raise_error(ActiveRecord::RecordInvalid, expected)
      end
    end

    context '부모 관계인 Facility와 WhichDirection를 미리 만들면' do
      # Facility
      let(:national_police_agency_id) { NationalPoliceAgency.create!({ name: 'p_agency1' }).id }
      let(:police_station_id) { PoliceStation.create!({ name: 'p_station1', national_police_agency_id: }).id }
      let(:management_agency_id) do
        ManagementAgency.create!({ name: 'm_agency1', national_police_agency_id:, police_station_id: }).id
      end
      let(:purpose_of_camera_installation_id) { PurposeOfCameraInstallation.create!({ purpose: 'purpose1' }).id }
      let(:facility_id) do
        Facility.create!({ name: 'facility1', management_agency_id:, purpose_of_camera_installation_id: }).id
      end
      # WhichDirection
      let(:which_direction_id) { WhichDirection.create!({ direction: 'direction1' }).id }
      # CameraLocation
      let(:create_param) { { location: 'location1', facility_id:, which_direction_id: } }
      let(:expected) { 1 }
      it 'create 가능' do
        CameraLocation.create!(create_param)
        actual = CameraLocation.all.length

        expect(actual).to equal(expected)
      end
    end
  end
end
