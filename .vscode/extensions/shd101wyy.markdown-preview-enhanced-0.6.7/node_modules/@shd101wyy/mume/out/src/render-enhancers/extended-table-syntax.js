"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
/**
 * Extend table syntax to support colspan and rowspan for merging cells
 * @param $
 */
function enhance($) {
    return __awaiter(this, void 0, void 0, function* () {
        const rowspans = []; // ^
        const colspans = []; // >
        const colspans2 = []; // empty
        $("table").each((i, table) => {
            const $table = $(table);
            let $prevRow = null;
            $table.children().each((a, headBody) => {
                const $headBody = $(headBody);
                $headBody.children().each((i2, row) => {
                    const $row = $(row);
                    $row.children().each((j, col) => {
                        const $col = $(col);
                        const text = $col.text();
                        if (!text.length) {
                            // merge to left
                            const $prev = $col.prev();
                            if ($prev.length) {
                                colspans2.push([$prev, $col]);
                                // const colspan = parseInt($prev.attr('colspan')) || 1
                                // $prev.attr('colspan', colspan+1)
                                // $col.remove()
                            }
                        }
                        else if (text.trim() === "^" && $prevRow) {
                            // merge to top
                            const $prev = $($prevRow.children()[j]);
                            if ($prev.length) {
                                rowspans.push([$prev, $col]);
                                // const rowspan = parseInt($prev.attr('rowspan')) || 1
                                // $prev.attr('rowspan', rowspan+1)
                                // $col.remove()
                            }
                        }
                        else if (text.trim() === ">") {
                            // merge to right
                            const $next = $col.next();
                            if ($next.length) {
                                // const colspan = parseInt($next.attr('colspan')) || 1
                                // $next.attr('colspan', colspan+1)
                                // $col.remove()
                                colspans.push([$col, $next]);
                            }
                        }
                    });
                    $prevRow = $row;
                });
            });
        });
        for (let i = rowspans.length - 1; i >= 0; i--) {
            const [$prev, $col] = rowspans[i];
            const rowspan = (parseInt($prev.attr("rowspan"), 10) || 1) +
                (parseInt($col.attr("rowspan"), 10) || 1);
            $prev.attr("rowspan", rowspan.toString());
            $col.remove();
        }
        // tslint:disable-next-line prefer-for-of
        for (let i = 0; i < colspans.length; i++) {
            const [$prev, $col] = colspans[i];
            const colspan = (parseInt($prev.attr("colspan"), 10) || 1) +
                (parseInt($col.attr("colspan"), 10) || 1);
            $col.attr("colspan", colspan.toString());
            $prev.remove();
        }
        for (let i = colspans2.length - 1; i >= 0; i--) {
            const [$prev, $col] = colspans2[i];
            const colspan = (parseInt($prev.attr("colspan"), 10) || 1) +
                (parseInt($col.attr("colspan"), 10) || 1);
            $prev.attr("colspan", colspan.toString());
            $col.remove();
        }
    });
}
exports.default = enhance;
//# sourceMappingURL=extended-table-syntax.js.map