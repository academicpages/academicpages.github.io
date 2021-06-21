/*
    Cparse.java -- Racc Runtime Core for JRuby
    
    Copyright (c) 2016 Charles Oliver Nutter <headius@headius.com>
    
    Ported from and distributed under the same licence as cparse.c
    
    cparse.c -- Racc Runtime Core
  
    Copyright (c) 1999-2006 Minero Aoki
  
    This library is free software.
    You can distribute/modify this program under the same terms of ruby.
*/
package com.headius.racc;

import org.jruby.Ruby;
import org.jruby.RubyArray;
import org.jruby.RubyBasicObject;
import org.jruby.RubyClass;
import org.jruby.RubyContinuation;
import org.jruby.RubyFixnum;
import org.jruby.RubyHash;
import org.jruby.RubyKernel;
import org.jruby.RubyModule;
import org.jruby.RubyNumeric;
import org.jruby.RubyObject;
import org.jruby.RubySymbol;
import org.jruby.anno.JRubyMethod;
import org.jruby.exceptions.JumpException;
import org.jruby.internal.runtime.methods.AttrReaderMethod;
import org.jruby.internal.runtime.methods.AttrWriterMethod;
import org.jruby.internal.runtime.methods.CallConfiguration;
import org.jruby.runtime.Arity;
import org.jruby.runtime.Block;
import org.jruby.runtime.BlockCallback;
import org.jruby.runtime.CallBlock19;
import org.jruby.runtime.CallSite;
import org.jruby.runtime.Helpers;
import org.jruby.runtime.MethodIndex;
import org.jruby.runtime.ObjectAllocator;
import org.jruby.runtime.Signature;
import org.jruby.runtime.ThreadContext;
import org.jruby.runtime.Visibility;
import org.jruby.runtime.builtin.IRubyObject;
import org.jruby.runtime.load.Library;

public class Cparse implements Library {
    public static final String RACC_VERSION = "1.4.15"; // TODO: parse from Cparse.c

    public enum TokenType {
        DEFAULT(-1),
        FINAL(0),
        ERROR(1);

        private final int id;
        TokenType(int id) { this.id = id; }
    }

    private RubyFixnum vDEFAULT_TOKEN;
    private RubyFixnum vERROR_TOKEN;
    private RubyFixnum vFINAL_TOKEN;

    private RubyClass RaccBug;
    private RubyClass CparseParams;

    private static final String ID_YYDEBUG = "@yydebug";
    private static final String ID_NEXTTOKEN = "next_token";
    private static final String ID_ONERROR = "on_error";
    private static final String ID_NOREDUCE = "_reduce_none";
    private static final String ID_ERRSTATUS = "@racc_error_status";

    private static final String ID_D_SHIFT = "racc_shift";
    private static final String ID_D_REDUCE = "racc_reduce";
    private static final String ID_D_ACCEPT = "racc_accept";
    private static final String ID_D_READ_TOKEN = "racc_read_token";
    private static final String ID_D_NEXT_STATE = "racc_next_state";
    private static final String ID_D_E_POP = "racc_e_pop";

    private RubySymbol sym_noreduce;
    private CallSite call_nexttoken;
    private CallSite call_onerror;
    private CallSite call_d_shift;
    private CallSite call_d_reduce;
    private CallSite call_d_accept;
    private CallSite call_d_read_token;
    private CallSite call_d_next_state;
    private CallSite call_d_e_pop;

    private static RubySymbol value_to_id(ThreadContext context, IRubyObject v) {
        if (!(v instanceof RubySymbol)) {
            throw context.runtime.newTypeError("not symbol");
        }
        return (RubySymbol)v;
    }

    private static int num_to_int(IRubyObject n) {
        return assert_integer(n);
    }

    private static IRubyObject AREF(ThreadContext context, IRubyObject s, int idx) {
        return ((0 <= idx && idx < ((RubyArray)s).size()) ? ((RubyArray)s).entry(idx) : context.nil);
    }

    private static IRubyObject get_stack_tail(ThreadContext context, RubyArray stack, int len) {
        if (len < 0) return context.nil;
        int size = stack.size();
        len = Math.min(len, size);
        return stack.subseq(size - len, len);
    }

    private static void cut_stack_tail(ThreadContext context, RubyArray stack, int len) {
        while (len > 0) {
            stack.pop(context);
            len--;
        }
    }

    private static final int STACK_INIT_LEN = 64;
    private static RubyArray NEW_STACK(ThreadContext context) {
        return context.runtime.newArray(STACK_INIT_LEN);
    }
    private static IRubyObject PUSH(RubyArray stack, IRubyObject i) {
        return stack.append(i);
    }
    private static IRubyObject POP(ThreadContext context, RubyArray stack) {
        return stack.pop(context);
    }
    private static IRubyObject LAST_I(ThreadContext context, RubyArray stack) {
        return stack.size() > 0 ? stack.last() : context.nil;
    }
    private static IRubyObject GET_TAIL(ThreadContext context, RubyArray stack, int len) {
        return get_stack_tail(context, stack, len);
    }
    private static void CUT_TAIL(ThreadContext context, RubyArray stack, int len) {
        cut_stack_tail(context, stack, len);
    }

    static final int CP_FIN_ACCEPT = 1;
    static final int CP_FIN_EOT = 2;
    static final int CP_FIN_CANTPOP = 3;

    public class CparseParams extends RubyObject {
        public CparseParams(Ruby runtime, RubyClass rubyClass) {
            super(runtime, rubyClass);
        }

        public void initialize_params(ThreadContext context, Parser parser, IRubyObject arg, IRubyObject lexer, IRubyObject lexmid) {
            Ruby runtime = context.runtime;
            this.parser = parser;
            this.lexer = lexer;
            if (!lexmid.isNil()) {
                this.lexmid = value_to_id(context, lexmid);
                this.call_lexmid = MethodIndex.getFunctionalCallSite(this.lexmid.toString());
            }

            this.debug           = parser.getInstanceVariable(ID_YYDEBUG).isTrue();

            RubyArray argAry = arg.convertToArray();
            if (!(13 <= argAry.size() && argAry.size() <= 14)) {
                throw runtime.newRaiseException(RaccBug, "[Racc Bug] wrong arg.size " + argAry.size());
            }
            this.action_table     = assert_array(argAry.eltOk(0));
            this.action_check     = assert_array(argAry.eltOk(1));
            this.action_default   = assert_array(argAry.eltOk(2));
            this.action_pointer   = assert_array(argAry.eltOk(3));
            this.goto_table       = assert_array(argAry.eltOk(4));
            this.goto_check       = assert_array(argAry.eltOk(5));
            this.goto_default     = assert_array(argAry.eltOk(6));
            this.goto_pointer     = assert_array(argAry.eltOk(7));
            this.nt_base          = assert_integer(argAry.eltOk(8));
            this.reduce_table     = assert_array(argAry.eltOk(9));
            this.token_table      = assert_hash(argAry.eltOk(10));
            this.shift_n          = assert_integer(argAry.eltOk(11));
            this.reduce_n         = assert_integer(argAry.eltOk(12));
            if (argAry.size() > 13) {
                this.use_result_var = argAry.eltOk(13).isTrue();
             } else {
                this.use_result_var = true;
            }

            this.tstack          = this.debug ? NEW_STACK(context) : null;
            this.vstack          = NEW_STACK(context);
            this.state           = NEW_STACK(context);
            this.curstate        = 0;
            PUSH(this.state, RubyFixnum.zero(runtime));
            this.t               = runtime.newFixnum(TokenType.FINAL.id + 1); // must not init to FINAL_TOKEN
            this.nerr            = 0;
            this.errstatus       = 0;
            this.parser.setInstanceVariable(ID_ERRSTATUS, runtime.newFixnum(this.errstatus));

            this.retval          = context.nil;
            this.fin             = 0;

            this.lex_is_iterator = false;

            parser.setInstanceVariable("@vstack", this.vstack);
            if (this.debug) {
                parser.setInstanceVariable("@tstack", this.tstack);
            }
            else {
                parser.setInstanceVariable("@tstack", context.nil);
            }
        }

        public void extract_user_token(ThreadContext context, IRubyObject block_args, IRubyObject[] tokVal) {
            if (block_args.isNil()) {
                /* EOF */
                tokVal[0] = context.runtime.getFalse();
                tokVal[1] = context.runtime.newString("$");
                return;
            }

            if (!(block_args instanceof RubyArray)) {
                throw context.runtime.newTypeError(
                        (lex_is_iterator ? lexmid.asJavaString() : "next_token") +
                                " " +
                                (lex_is_iterator ? "yielded" : "returned") +
                                " " +
                                block_args.getMetaClass().getName() +
                                " (must be Array[2])");
            }
            RubyArray block_args_ary = (RubyArray)block_args;
            if (block_args_ary.size() != 2) {
                throw context.runtime.newTypeError(
                        (lex_is_iterator ? lexmid.asJavaString() : "next_token") +
                                " " +
                                (lex_is_iterator ? "yielded" : "returned") +
                                " wrong size of array (" +
                                block_args_ary.size() +
                                " for 2)");
            }
            tokVal[0] = ((RubyArray) block_args).eltOk(0);
            tokVal[1] = ((RubyArray) block_args).eltOk(1);
        }

        private static final int RESUME = 1;
        private static final int NOTFOUND = 2;
        private static final int ERROR_RECOVERED = 3;
        private static final int ERROR = 4;
        private static final int HANDLE_ACT = 5;
        private static final int ACT_FIXED = 6;
        private static final int ACCEPT = 7;
        private static final int USER_YYERROR = 8;
        private static final int ERROR_POP = 9;
        private static final int TRANSIT = 9;

        private void SHIFT(ThreadContext context, int act, IRubyObject tok, IRubyObject val) {
            shift(context, act, tok, val);
        }

        public void parse_main(ThreadContext context, IRubyObject tok, IRubyObject val, boolean resume) {
            Ruby runtime = context.runtime;

            int i = 0;              /* table index */
            int act = 0;            /* action type */
            IRubyObject act_value;     /* action type, VALUE version */
            boolean read_next = true;   /* true if we need to read next token */
            IRubyObject tmp;

            int branch = 0;

            if (resume) {
                branch = RESUME;
            }

            BRANCH: while (true) {
                switch (branch) {
                    case 0:

                        D_puts("");
                        D_puts("---- enter new loop ----");
                        D_puts("");

                        D_printf("(act) k1=%ld\n", this.curstate);
                        tmp = AREF(context, this.action_pointer, this.curstate);
                        if (tmp.isNil()) {branch = NOTFOUND; continue BRANCH;}
                        D_puts("(act) pointer[k1] ok");
                        i = assert_integer(tmp);

                        D_printf("read_next=%d\n", read_next);
                        if (read_next && (!this.t.equals(vFINAL_TOKEN))) {
                            if (this.lex_is_iterator) {
                                D_puts("resuming...");
                                if (this.fin != 0) throw runtime.newArgumentError("token given after EOF");
                                this.i = i;  /* save i */
                                return;

                                // remainder of case duplicated from here for RESUME case
                                //D_puts(this, "resumed");
                                //i = this.i;  /* load i */
                            }
                            else {
                                D_puts("next_token");
                                tmp = call_nexttoken.call(context, this.parser, this.parser);
                                IRubyObject[] tokVal = {tok, val};
                                extract_user_token(context, tmp, tokVal);
                                tok = tokVal[0];
                                val = tokVal[1];
                            }
                            /* convert token */
                            this.t = ((RubyHash)this.token_table).op_aref(context, tok);
                            if (this.t.isNil()) {
                                this.t = vERROR_TOKEN;
                            }
                            D_printf("(act) t(k2)=%ld\n", assert_integer(this.t));
                            if (this.debug) {
                                call_d_read_token.call(context, this.parser, this.parser, this.t, tok, val);
                            }
                        }

                        // duplicated logic from above for RESUME case
                    case RESUME:
                        if (branch == RESUME) {
                            D_puts("resumed");
                            i = this.i;  /* load i */

                            /* convert token */
                            this.t = ((RubyHash)this.token_table).op_aref(context, tok);
                            if (this.t.isNil()) {
                                this.t = vERROR_TOKEN;
                            }
                            D_printf("(act) t(k2)=%ld\n", assert_integer(this.t));
                            if (this.debug) {
                                call_d_read_token.call(context, this.parser, this.parser, this.t, tok, val);
                            }
                        }

                        read_next = false;

                        i += assert_integer(this.t);
                        D_printf("(act) i=%ld\n", i);
                        if (i < 0) {branch = NOTFOUND; continue BRANCH;}

                        act_value = AREF(context, this.action_table, i);
                        if (act_value.isNil()) {branch = NOTFOUND; continue BRANCH;}
                        act = assert_integer(act_value);
                        D_printf("(act) table[i]=%ld\n", act);

                        tmp = AREF(context, this.action_check, i);
                        if (tmp.isNil()) {branch = NOTFOUND; continue BRANCH;}
                        if (assert_integer(tmp) != this.curstate) {branch = NOTFOUND; continue BRANCH;}
                        D_printf("(act) check[i]=%ld\n", assert_integer(tmp));

                        D_puts("(act) found");

                    case ACT_FIXED:
                        D_printf("act=%ld\n", act);
                        branch = HANDLE_ACT; continue BRANCH;

                    case NOTFOUND:
                        D_puts("(act) not found: use default");
                        act_value = AREF(context, this.action_default, this.curstate);
                        act = assert_integer(act_value);
                        branch = ACT_FIXED; continue BRANCH;

                    case HANDLE_ACT:
                        if (act > 0 && act < this.shift_n) {
                            D_puts("shift");
                            if (this.errstatus > 0) {
                                this.errstatus--;
                                this.parser.setInstanceVariable(ID_ERRSTATUS, runtime.newFixnum(this.errstatus));
                            }
                            SHIFT(context, act, this.t, val);
                            read_next = true;
                        }
                        else if (act < 0 && act > -(this.reduce_n)) {
                            D_puts("reduce");
                            { // macro REDUCE
                                switch (reduce(context, act)) {
                                    case 0: /* normal */
                                        break;
                                    case 1: /* yyerror */
                                        branch = USER_YYERROR;
                                        continue BRANCH;
                                    case 2: /* yyaccept */
                                        D_puts("u accept");
                                        branch = ACCEPT;
                                        continue BRANCH;
                                    default:
                                        break;
                                }
                            }
                        }
                        else if (act == -(this.reduce_n)) {
                            branch = ERROR; continue BRANCH;
                        }
                        else if (act == this.shift_n) {
                            D_puts("accept");
                            branch = ACCEPT; continue BRANCH;
                        }
                        else {
                            throw runtime.newRaiseException(RaccBug, "[Cparse Bug] unknown act value " + act);
                        }

                        // fall through
                    case ERROR_RECOVERED:

                        if (this.debug) {
                            call_d_next_state.call(context, this.parser, this.parser, runtime.newFixnum(this.curstate), this.state);
                        }
                        branch = 0; continue BRANCH;

                    /* not reach */

                    case ACCEPT:
                        if (this.debug) call_d_accept.call(context, this.parser, this.parser);
                        this.retval = this.vstack.eltOk(0);
                        this.fin = CP_FIN_ACCEPT;
                        return;

                    case ERROR:
                        D_printf("error detected, status=%ld\n", this.errstatus);
                        if (this.errstatus == 0) {
                            this.nerr++;
                            call_onerror.call(context, this.parser, this.parser, this.t, val, this.vstack);
                        }

                        // fall through
                    case USER_YYERROR:
                        if (this.errstatus == 3) {
                            if (this.t.equals(vFINAL_TOKEN)) {
                                this.retval = runtime.getFalse();
                                this.fin = CP_FIN_EOT;
                                return;
                            }
                            read_next = true;
                        }
                        this.errstatus = 3;
                        this.parser.setInstanceVariable(ID_ERRSTATUS, runtime.newFixnum(this.errstatus));

                        /* check if we can shift/reduce error token */
                        D_printf("(err) k1=%ld\n", this.curstate);
                        D_printf("(err) k2=%d (error)\n", TokenType.ERROR.id);

                        int branch2 = 0;

                        BRANCH2: while (true) {
                            switch (branch2) {
                                case 0:
                                    tmp = AREF(context, this.action_pointer, this.curstate);
                                    if (tmp.isNil()) {branch2 = ERROR_POP; continue BRANCH2;}
                                    D_puts("(err) pointer[k1] ok");

                                    i = assert_integer(tmp) + TokenType.ERROR.id;
                                    D_printf("(err) i=%ld\n", i);
                                    if (i < 0) {branch2 = ERROR_POP; continue BRANCH2;}

                                    act_value = AREF(context, this.action_table, i);
                                    if (act_value.isNil()) {
                                        D_puts("(err) table[i] == nil");
                                        branch2 = ERROR_POP; continue BRANCH2;
                                    }
                                    act = assert_integer(act_value);
                                    D_printf("(err) table[i]=%ld\n", act);

                                    tmp = AREF(context, this.action_check, i);
                                    if (tmp.isNil()) {
                                        D_puts("(err) check[i] == nil");
                                        branch2 = ERROR_POP; continue BRANCH2;
                                    }
                                    if (assert_integer(tmp) != this.curstate) {
                                        D_puts("(err) check[i] != k1");
                                        branch2 = ERROR_POP; continue BRANCH2;
                                    }

                                    D_puts("(err) found: can handle error token");
                                    break BRANCH2;

                                case ERROR_POP:
                                    D_puts("(err) act not found: can't handle error token; pop");

                                    if (this.state.size() <= 1) {
                                        this.retval = context.nil;
                                        this.fin = CP_FIN_CANTPOP;
                                        return;
                                    }
                                    POP(context, this.state);
                                    POP(context, this.vstack);
                                    this.curstate = assert_integer(LAST_I(context, this.state));
                                    if (this.debug) {
                                        POP(context, this.tstack);
                                        call_d_e_pop.call(context, this.parser, this.parser, this.state, this.tstack, this.vstack);
                                    }
                            }
                        }

                        /* shift/reduce error token */
                        if (act > 0 && act < this.shift_n) {
                            D_puts("e shift");
                            SHIFT(context, act, runtime.newFixnum(TokenType.ERROR.id), val);
                        }
                        else if (act < 0 && act > -(this.reduce_n)) {
                            D_puts("e reduce");
                            { // macro REDUCE
                                switch (reduce(context, act)) {
                                    case 0: /* normal */
                                        break;
                                    case 1: /* yyerror */
                                        branch = USER_YYERROR;
                                        continue BRANCH;
                                    case 2: /* yyaccept */
                                        D_puts("u accept");
                                        branch = ACCEPT;
                                        continue BRANCH;
                                    default:
                                        break;
                                }
                            }
                        }
                        else if (act == this.shift_n) {
                            D_puts("e accept");
                            branch = ACCEPT; continue BRANCH;
                        }
                        else {
                            throw runtime.newRaiseException(RaccBug, "[Cparse Bug] unknown act value " + act);
                        }
                        branch = ERROR_RECOVERED; continue BRANCH;
                }
            }
        }

        private void shift(ThreadContext context, int act, IRubyObject tok, IRubyObject val) {
            PUSH(vstack, val);
            if (debug) {
                PUSH(tstack, tok);
                call_d_shift.call(context, this.parser, this.parser, tok, tstack, vstack);
            }
            curstate = act;
            PUSH(state, context.runtime.newFixnum(curstate));
        }

        private int reduce(ThreadContext context, int act) {
            ruleno = -act * 3;
            IRubyObject tag = context.runtime.newSymbol("racc_jump");
            IRubyObject code = RubyKernel.rbCatch19(context, this,
                    tag,
                    CallBlock19.newCallClosure(this, getMetaClass(), Signature.NO_ARGUMENTS,
                            new BlockCallback() {
                                @Override
                                public IRubyObject call(ThreadContext context, IRubyObject[] args, Block block) {
                                    return reduce0(context);
                                }
                            }, context));
            errstatus = assert_integer(parser.getInstanceVariable(ID_ERRSTATUS));
            return assert_integer(code);
        }

        private IRubyObject reduce0(ThreadContext context) {
            Ruby runtime = context.runtime;

            IRubyObject reduce_to, reduce_len, method_id;
            int len;
            RubySymbol mid;
            IRubyObject tmp, tmp_t = RubyBasicObject.UNDEF, tmp_v = RubyBasicObject.UNDEF;
            int i, k1 = 0, k2;
            IRubyObject goto_state = context.nil;

            reduce_len = this.reduce_table.entry(this.ruleno);
            reduce_to  = this.reduce_table.entry(this.ruleno+1);
            method_id  = this.reduce_table.entry(this.ruleno+2);
            len = assert_integer(reduce_len);
            mid = value_to_id(context, method_id);

            int branch = 0;
            BRANCH: while (true) {
                switch (branch) {
                    case 0:

                        /* call action */
                        if (len == 0) {
                            tmp = context.nil;
                            if (!mid.equals(sym_noreduce))
                                tmp_v = runtime.newArray();
                            if (this.debug)
                                tmp_t = runtime.newArray();
                        }
                        else {
                            if (!mid.equals(sym_noreduce)) {
                                tmp_v = GET_TAIL(context, this.vstack, len);
                                tmp = ((RubyArray)tmp_v).entry(0);
                            }
                            else {
                                tmp = this.vstack.entry(this.vstack.size() - len);
                            }
                            CUT_TAIL(context, this.vstack, len);
                            if (this.debug) {
                                tmp_t = GET_TAIL(context, this.tstack, len);
                                CUT_TAIL(context, this.tstack, len);
                            }
                            CUT_TAIL(context, this.state, len);
                        }
                        if (!mid.equals(sym_noreduce)) {
                            if (this.use_result_var) {
                                tmp = Helpers.invoke(context, this.parser, mid.toString(), tmp_v, this.vstack, tmp);
                            }
                            else {
                                tmp = Helpers.invoke(context, this.parser, mid.toString(), tmp_v, this.vstack);
                            }
                        }

                        /* then push result */
                        PUSH(this.vstack, tmp);
                        if (this.debug) {
                            PUSH(this.tstack, reduce_to);
                            call_d_reduce.call(context, this.parser, this.parser, tmp_t, reduce_to, this.tstack, this.vstack);
                        }

                        /* calculate transition state */
                        if (state.size() == 0)
                            throw runtime.newRaiseException(RaccBug, "state stack unexpectedly empty");
                        k2 = assert_integer(LAST_I(context, this.state));
                        k1 = assert_integer(reduce_to) - this.nt_base;
                        D_printf("(goto) k1=%ld\n", k1);
                        D_printf("(goto) k2=%ld\n", k2);

                        tmp = AREF(context, this.goto_pointer, k1);
                        if (tmp.isNil()) {branch = NOTFOUND; continue BRANCH;}

                        i = assert_integer(tmp) + k2;
                        D_printf("(goto) i=%ld\n", i);
                        if (i < 0) {branch = NOTFOUND; continue BRANCH;}

                        goto_state = AREF(context, this.goto_table, i);
                        if (goto_state.isNil()) {
                            D_puts("(goto) table[i] == nil");
                            branch = NOTFOUND; continue BRANCH;
                        }
                        D_printf("(goto) table[i]=%ld (goto_state)\n", goto_state.convertToInteger().getLongValue());

                        tmp = AREF(context, this.goto_check, i);
                        if (tmp.isNil()) {
                            D_puts("(goto) check[i] == nil");
                            branch = NOTFOUND; continue BRANCH;
                        }
                        if (!tmp.equals(runtime.newFixnum(k1))) {
                            D_puts("(goto) check[i] != table[i]");
                            branch = NOTFOUND; continue BRANCH;
                        }
                        D_printf("(goto) check[i]=%ld\n", tmp.convertToInteger().getLongValue());

                        D_puts("(goto) found");

                    case TRANSIT:
                        PUSH(this.state, goto_state);
                        this.curstate = assert_integer(goto_state);
                        return RubyFixnum.zero(runtime);

                    case NOTFOUND:
                        D_puts("(goto) not found: use default");
                        /* overwrite `goto-state' by default value */
                        goto_state = AREF(context, this.goto_default, k1);
                        branch = TRANSIT; continue BRANCH;
                }
            }
        }

        private void D_puts(String msg) {
            if (sys_debug) {
                System.out.println(msg);
            }
        }

        private void D_printf(String fmt, long arg) {
            if (sys_debug) {
                System.out.println(fmt + ": " + arg);
            }
        }

        private void D_printf(String fmt, boolean arg) {
            if (sys_debug) {
                System.out.println(fmt + ": " + arg);
            }
        }

        Parser parser;          /* parser object */

        boolean lex_is_iterator;
        IRubyObject lexer;           /* scanner object */
        RubySymbol lexmid;          /* name of scanner method (must be an iterator) */
        CallSite call_lexmid;       /* call site for scanner method */

        /* State transition tables (immutable)
           Data structure is from Dragon Book 4.9 */
        /* action table */
        IRubyObject action_table;
        IRubyObject action_check;
        IRubyObject action_default;
        IRubyObject action_pointer;
        /* goto table */
        IRubyObject goto_table;
        IRubyObject goto_check;
        IRubyObject goto_default;
        IRubyObject goto_pointer;

        int nt_base;         /* NonTerminal BASE index */
        RubyArray reduce_table;    /* reduce data table */
        IRubyObject token_table;     /* token conversion table */

        /* parser stacks and parameters */
        RubyArray state;
        int curstate;
        RubyArray vstack;
        RubyArray tstack;
        IRubyObject t;
        int shift_n;
        int reduce_n;
        int ruleno;

        int errstatus;         /* nonzero in error recovering mode */
        int nerr;              /* number of error */

        boolean use_result_var;

        IRubyObject retval;           /* return IRubyObject of parser routine */
        int fin;               /* parse result status */

        boolean debug;              /* user level debug */
        boolean sys_debug;          /* system level debug */

        int i;                 /* table index */
    }

    private static RubyArray assert_array(IRubyObject a) {
        return a.convertToArray();
    }

    private static RubyHash assert_hash(IRubyObject h) {
        return h.convertToHash();
    }

    private static int assert_integer(IRubyObject i) {
        return (int)i.convertToInteger().getLongValue();
    }

    public class Parser extends RubyObject {
        public Parser(Ruby runtime, RubyClass rubyClass) {
            super(runtime, rubyClass);
        }

        public static final String Racc_Runtime_Core_Version_C = RACC_VERSION;
        public static final String Racc_Runtime_Core_Id_C = "$originalId: cparse.c,v 1.8 2006/07/06 11:39:46 aamine Exp $";

        @JRubyMethod(name = "_racc_do_parse_c", frame = true)
        public IRubyObject racc_cparse(ThreadContext context, IRubyObject arg, IRubyObject sysdebug) {
            CparseParams v = new CparseParams(context.runtime, CparseParams);

            v.D_puts("starting cparse");
            v.sys_debug = sysdebug.isTrue();
            v.initialize_params(context, this, arg, context.nil, context.nil);
            v.lex_is_iterator = false;
            v.parse_main(context, context.nil, context.nil, false);

            return v.retval;
        }

        @JRubyMethod(name = "_racc_yyparse_c", frame = true, required = 4)
        public IRubyObject racc_yyparse(ThreadContext context, IRubyObject[] args) {
            Ruby runtime = context.runtime;
            CparseParams v = new CparseParams(context.runtime, CparseParams);

            IRubyObject lexer = args[0], lexmid = args[1], arg = args[2], sysdebug = args[3];

            v.sys_debug = sysdebug.isTrue();
            v.D_puts("start C yyparse");
            v.initialize_params(context, this, arg, lexer, lexmid);
            v.lex_is_iterator = true;
            v.D_puts("params initialized");
            v.parse_main(context, context.nil, context.nil, false);
            call_lexer(context, v);
            if (v.fin == 0) {
                throw runtime.newArgumentError(v.lexmid + " is finished before EndOfToken");
            }

            return v.retval;
        }

        private class LexerUnroll extends RuntimeException {
            public Throwable fillInStackTrace() {
                return this;
            }
        }

        private void call_lexer(ThreadContext context, final CparseParams v) {
            final LexerUnroll lexerUnroll = new LexerUnroll();
            try {
                v.call_lexmid.call(context, v.lexer, v.lexer, CallBlock19.newCallClosure(v, v.getMetaClass(), Arity.ONE_ARGUMENT, new BlockCallback() {
                    @Override
                    public IRubyObject call(ThreadContext context, IRubyObject[] args, Block block) {
                        Ruby runtime = context.getRuntime();
                        if (v.fin != 0) {
                            throw runtime.newArgumentError("extra token after EndOfToken");
                        }
                        IRubyObject[] tokVal = {null, null};
                        v.extract_user_token(context, args[0], tokVal);
                        v.parse_main(context, tokVal[0], tokVal[1], true);
                        if (v.fin != 0 && v.fin != CP_FIN_ACCEPT) {
                            throw lexerUnroll;
                        }

                        return context.nil;
                    }
                }, context));
            } catch (LexerUnroll maybeOurs) {
                if (maybeOurs.equals(lexerUnroll)) {
                    return;
                }
            }
        }
    }

    public void load(Ruby runtime, boolean wrap) {
        RubyModule racc = runtime.getOrCreateModule("Racc");
        RubyClass parser = racc.defineOrGetClassUnder("Parser", runtime.getObject());
        parser.setAllocator(new ObjectAllocator() {
            @Override
            public IRubyObject allocate(Ruby ruby, RubyClass rubyClass) {
                return new Parser(ruby, rubyClass);
            }
        });

        parser.defineAnnotatedMethods(Parser.class);

        parser.defineConstant("Racc_Runtime_Core_Version_C", runtime.newString(Parser.Racc_Runtime_Core_Version_C));
        parser.defineConstant("Racc_Runtime_Core_Id_C", runtime.newString(Parser.Racc_Runtime_Core_Id_C));

        CparseParams = racc.defineClassUnder("CparseParams", runtime.getObject(), new ObjectAllocator() {
            @Override
            public IRubyObject allocate(Ruby ruby, RubyClass rubyClass) {
                return new CparseParams(ruby, rubyClass);
            }
        });

        RaccBug = runtime.getRuntimeError();
        sym_noreduce = runtime.newSymbol(ID_NOREDUCE);
        call_nexttoken = MethodIndex.getFunctionalCallSite(ID_NEXTTOKEN);
        call_onerror = MethodIndex.getFunctionalCallSite(ID_ONERROR);
        call_d_shift = MethodIndex.getFunctionalCallSite(ID_D_SHIFT);
        call_d_reduce = MethodIndex.getFunctionalCallSite(ID_D_REDUCE);
        call_d_accept = MethodIndex.getFunctionalCallSite(ID_D_ACCEPT);
        call_d_read_token = MethodIndex.getFunctionalCallSite(ID_D_READ_TOKEN);
        call_d_next_state = MethodIndex.getFunctionalCallSite(ID_D_NEXT_STATE);
        call_d_e_pop = MethodIndex.getFunctionalCallSite(ID_D_E_POP);

        vDEFAULT_TOKEN      = runtime.newFixnum(TokenType.DEFAULT.id);
        vERROR_TOKEN      = runtime.newFixnum(TokenType.ERROR.id);
        vFINAL_TOKEN      = runtime.newFixnum(TokenType.FINAL.id);
    }
}
