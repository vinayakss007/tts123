import Button from '@/components/common/Button';
import Input from '@/components/common/Input';
import { useAuthStore } from '@/store/authStore';

export default function Settings() {
  const { user } = useAuthStore();

  return (
    <div className="space-y-6 max-w-2xl">
      <h1 className="text-2xl font-bold">Settings</h1>
      <div className="card">
        <h2 className="font-medium mb-4">Profile</h2>
        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <Input label="First Name" defaultValue={user?.first_name} />
            <Input label="Last Name" defaultValue={user?.last_name} />
          </div>
          <Input label="Email" defaultValue={user?.email} disabled />
          <Button>Save Changes</Button>
        </div>
      </div>
      <div className="card">
        <h2 className="font-medium mb-4">Organization</h2>
        <Input label="Organization Name" defaultValue="My Workspace" />
        <Button className="mt-4">Update Organization</Button>
      </div>
    </div>
  );
}
