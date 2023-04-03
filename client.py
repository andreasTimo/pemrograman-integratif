import grpc
import equipment_pb2
import equipment_pb2_grpc

def run():
    # membuat koneksi ke server
    channel = grpc.insecure_channel('localhost:50051')
    stub = equipment_pb2_grpc.EquipmentServiceStub(channel)

    # memanggil fungsi CreateEquipment
    response = stub.CreateEquipment(equipment_pb2.Equipment(name='name', type='cek', quantity=1))
    print("CreateEquipment Response:", response)

    # memanggil fungsi ReadEquipment
    response = stub.ReadEquipment(equipment_pb2.Equipment(name='name'))
    print("ReadEquipment Response:", response)

    # memanggil fungsi UpdateEquipment
    response = stub.UpdateEquipment(equipment_pb2.Equipment(name='name', type='Aku', quantity=2))
    print("UpdateEquipment Response:", response)

    # memanggil fungsi DeleteEquipment
    response = stub.DeleteEquipment(equipment_pb2.Equipment(name='name'))
    print("DeleteEquipment Response:", response)

if __name__ == '__main__':
    run()
