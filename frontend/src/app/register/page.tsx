"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import Cookies from "js-cookie";
import Link from "next/link";
import api from "@/lib/api";
import { Button } from "@/components/ui/button";
import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

export default function RegisterPage() {
    const router = useRouter();
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleRegister = async (e: React.FormEvent) => {
        e.preventDefault();
        setIsLoading(true);
        setError(null);

        try {
            const response = await api.post("/auth/register", {
                name,
                email,
                password,
            });

            // Assume backend returns { token: "..." }
            if (response.data.token) {
                Cookies.set("token", response.data.token, { expires: 7 });
                router.push("/dashboard");
            } else {
                setError("Invalid response from server.");
            }
        } catch (err: any) {
            if (err.response?.data?.error) {
                setError(err.response.data.error);
            } else {
                setError("An unexpected error occurred during registration.");
            }
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex min-h-screen items-center justify-center bg-muted/40 p-4">
            <Card className="w-full max-w-sm">
                <CardHeader>
                    <CardTitle className="text-2xl">Create an account</CardTitle>
                    <CardDescription>
                        Enter your details below to create your account.
                    </CardDescription>
                </CardHeader>
                <form onSubmit={handleRegister}>
                    <CardContent className="space-y-4">
                        {error && (
                            <div className="p-3 text-sm text-red-500 bg-red-100 rounded-md">
                                {error}
                            </div>
                        )}
                        <div className="space-y-2">
                            <Label htmlFor="name">Full Name</Label>
                            <Input
                                id="name"
                                placeholder="John Doe"
                                required
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                disabled={isLoading}
                            />
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="email">Email</Label>
                            <Input
                                id="email"
                                type="email"
                                placeholder="m@example.com"
                                required
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                disabled={isLoading}
                            />
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="password">Password</Label>
                            <Input
                                id="password"
                                type="password"
                                required
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                disabled={isLoading}
                            />
                        </div>
                    </CardContent>
                    <CardFooter className="flex flex-col space-y-4">
                        <Button type="submit" className="w-full" disabled={isLoading}>
                            {isLoading ? "Creating account..." : "Sign Up"}
                        </Button>
                        <div className="text-center text-sm">
                            Already have an account?{" "}
                            <Link href="/login" className="underline">
                                Sign in
                            </Link>
                        </div>
                    </CardFooter>
                </form>
            </Card>
        </div>
    );
}
