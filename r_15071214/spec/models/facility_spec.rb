require 'rails_helper'

RSpec.describe Facility do
  describe '#create' do
    context '부모 관계인 ManagementAgency와 PurposeOfCameraInstallation를 미리 만들지 않아서' do
      let(:create_param) do
        { name: 'facility1', number_of_cameras: 2, management_agency_id: 1, purpose_of_camera_installation_id: 1 }
      end
      let(:expected) { 'Validation failed: Management agency must exist, Purpose of camera installation must exist' }
      it 'create 불가능' do
        expect { Facility.create!(create_param) }.to raise_error(ActiveRecord::RecordInvalid, expected)
      end
    end

    context '부모 관계인 NationalPoliceAgency를 미리 만들면' do
      # NationalPoliceAgency
      let(:national_police_agency_id) { NationalPoliceAgency.create!({ name: 'p_agency1' }).id }
      let(:police_station_id) { PoliceStation.create!({ name: 'p_station1', national_police_agency_id: }).id }
      let(:management_agency_id) do
        ManagementAgency.create!({ name: 'm_agency1', national_police_agency_id:, police_station_id: }).id
      end
      let(:purpose_of_camera_installation_id) { PurposeOfCameraInstallation.create!({ purpose: 'purpose1' }).id }
      # Facility
      let(:create_param) do
        { name: 'facility1', number_of_cameras: 2, management_agency_id:, purpose_of_camera_installation_id: }
      end
      let(:expected) { 1 }
      it 'create 가능' do
        Facility.create!(create_param)
        actual = Facility.all.length

        expect(actual).to equal(expected)
      end
    end
  end
end
