import { SignIn } from "@clerk/nextjs";

export default function LoginPage() {
    return (
        <div className="flex min-h-screen items-center justify-center p-4">
            <SignIn
                appearance={{
                    elements: {
                        formButtonPrimary:
                            "bg-slate-50 hover:bg-slate-200 text-slate-900 border-transparent",
                        card: "bg-slate-900 border border-slate-800",
                        headerTitle: "text-slate-50",
                        headerSubtitle: "text-slate-400",
                        socialButtonsBlockButton:
                            "bg-slate-900 border-slate-700 hover:bg-slate-800 text-slate-50 text-sm",
                        socialButtonsBlockButtonText: "text-slate-50 font-normal",
                        socialButtonsBlockButtonArrow: "text-slate-50",
                        dividerLine: "bg-slate-800",
                        dividerText: "text-slate-500",
                        formFieldLabel: "text-slate-200",
                        formFieldInput: "bg-slate-950 border-slate-800 text-slate-50 focus:ring-slate-400",
                        footerActionText: "text-slate-400",
                        footerActionLink: "text-slate-50 hover:text-slate-200"
                    },
                }}
            />
        </div>
    );
}
