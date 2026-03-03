import { SignUp } from "@clerk/nextjs";

export default function RegisterPage() {
    return (
        <div className="flex min-h-screen items-center justify-center p-4">
            <SignUp routing="path" path="/register" forceRedirectUrl="/dashboard" />
        </div>
    );
}
